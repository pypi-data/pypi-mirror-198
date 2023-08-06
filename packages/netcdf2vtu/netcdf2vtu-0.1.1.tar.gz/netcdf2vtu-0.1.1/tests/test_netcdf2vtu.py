# -*- coding: utf-8 -*-
"""These are the unit tests of the netcdf2vtu module."""

import os
from pytest import raises
import subprocess
import shlex

from netCDF4 import Dataset
from numpy import array, ndarray
from numpy.testing import assert_array_almost_equal
import vtk
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid, vtkPolyData
from vtkmodules.vtkFiltersPoints import vtkVoronoiKernel, vtkGaussianKernel, vtkShepardKernel
from vtk.numpy_interface import dataset_adapter as dsa

import netcdf2vtu.netcdf2vtu as n2v


nc_file1 = "data/ex1_3.nc"
nc_file2 = "data/ex2_4.nc"

in_vtu_path = "data/ogs.vtu"
out_vtu_path_mapper = "temp_mapper.vtu"
out_vtp_path_mapper = "temp_mapper.vtp"
out_vtu_path_fun = "temp_fun.vtu"
out_vtp_path_fun =  "temp_fun.vtp"
out_vtu_path_cli = "temp_cli.vtu"
ref_vtp_path = "tests/ref.vtp"
ref_vtu_path = "tests/ref.vtu"
data_var_names = ["SWC_L01", "SWC_L02"]
map_func_type = 1
nc_crs = "EPSG:4326"
vtu_crs = "EPSG:5684"
nullvalue = -9999
coordnames = ["lat", "lon", "time"]

class TestMapper():

    def setup_method(self):
        self.nc_file = nc_file1
        self.nc_data_var = data_var_names
        self.vtu_in = in_vtu_path
        self.vtu_out = out_vtu_path_mapper
        self.vtp_out = out_vtp_path_mapper
        self.nc_crs = nc_crs
        self.vtu_crs = vtu_crs
        self.map_func_type = map_func_type
        self.nullval = nullvalue
        self.coordnames = coordnames

        self.dataset = Dataset(self.nc_file, mode = "r", format = "NETCDF4")
        self.vtu = n2v.read_vtu(self.vtu_in)

        self.mapper = n2v.Mapper(
            nc_path = self.nc_file,
            vtu_path = self.vtu_in,
            data_var_names = self.nc_data_var,
            map_func_type = self.map_func_type,
            nc_crs = self.nc_crs,
            vtu_crs = self.vtu_crs,
            nullvalue = self.nullval
        )

        self.lat_dat = self.dataset.variables[self.coordnames[0]][:].filled()
        self.lon_dat = self.dataset.variables[self.coordnames[1]][:].filled()
        self.time_dat = self.dataset.variables[self.coordnames[2]][:].filled()

        self.nc_data = n2v.get_nc_data(self.dataset, self.nc_data_var)


    def test_init_mapper(self):

        mapper = n2v.Mapper(
            nc_path = self.nc_file,
            vtu_path = self.vtu_in,
            data_var_names = self.nc_data_var,
            map_func_type = self.map_func_type,
            nc_crs = self.nc_crs,
            vtu_crs = self.vtu_crs,
            nullvalue = self.nullval
        )

        assert type(mapper) is n2v.Mapper

        assert mapper.nc["path"] == self.nc_file
        assert mapper.nc["crs"] == self.nc_crs
        assert mapper.nc["data_names"] == self.nc_data_var
        assert type(mapper.nc["dataset"]) == type(self.dataset)

        assert mapper.in_vtu["path"] == self.vtu_in
        assert mapper.in_vtu["crs"] == self.vtu_crs
        assert type(mapper.in_vtu["vtu"]) == type(self.vtu)

        assert mapper.map_func_type == self.map_func_type
        assert mapper.nullvalue == self.nullval


    def test_map(self, tmp_path):

        a, b, c = self.coordnames
        vtu_path = str(tmp_path/self.vtu_out)
        vtp_path = str(tmp_path/self.vtp_out)

        self.mapper.map(vtu_path, a, b, c)
        self.mapper.write_vtp(vtp_path)

        # check variable names
        assert isinstance(self.mapper.nc["coord_names"], dict)
        assert self.mapper.nc["coord_names"]["lat_name"] == self.coordnames[0]
        assert self.mapper.nc["coord_names"]["lon_name"] == self.coordnames[1]
        assert self.mapper.nc["coord_names"]["time_name"] == self.coordnames[2]

        assert self.mapper.nc["data_names"] == self.nc_data_var

        # check coordinate data
        self.mapper.nc["coords"]["lat"] = self.lat_dat
        self.mapper.nc["coords"]["lon"] = self.lon_dat
        self.mapper.nc["coords"]["time"] = self.time_dat

        # check extracted data
        assert_array_almost_equal(
            self.mapper.nc["data"][0][1],
            self.nc_data[0][1]
        )

        assert_array_almost_equal(
            self.mapper.nc["data"][1][1],
            self.nc_data[1][1]
        )

        # check created vtp and vtu
        isinstance(self.mapper.vtp, vtkPolyData)
        isinstance(self.mapper.out_vtu, vtkUnstructuredGrid)

        # check written files
        os.path.isfile(vtu_path)
        os.path.isfile(vtp_path)


class TestFunctions():

    def setup_method(self):
        # specifictaion for input and output files
        self.nc_file = nc_file1
        self.nc_data_var = data_var_names
        self.vtu_in = in_vtu_path
        self.vtu_out = out_vtu_path_fun
        self.vtu_ref_path = ref_vtu_path
        self.vtp_ref = ref_vtp_path
        self.vtp_out = out_vtp_path_fun
        self.nc_crs = nc_crs
        self.vtu_crs = vtu_crs
        self.map_func_type = map_func_type
        self.nullval = nullvalue
        # read reference netcdf file and extract data
        self.dataset = Dataset(self.nc_file, mode = "r", format = "NETCDF4")
        self.swcl01 = self.dataset.variables["SWC_L01"][:].filled()
        self.swcl02 = self.dataset.variables["SWC_L02"][:].filled()
        self.coordnames = coordnames
        self.lat_dat = self.dataset.variables[self.coordnames[0]][:].filled()
        self.lon_dat = self.dataset.variables[self.coordnames[1]][:].filled()
        self.time_dat = self.dataset.variables[self.coordnames[2]][:].filled()
        # create reference vtp
        rdr = vtk.vtkXMLPolyDataReader()
        rdr.SetFileName(self.vtp_ref)
        rdr.Update()
        self.ref_vtp = rdr.GetOutput()
        self.ref_vtp_dsa = dsa.WrapDataObject(self.ref_vtp)
        # read reference vtu
        dst = vtk.vtkXMLUnstructuredGridReader()
        dst.SetFileName(self.vtu_ref_path)
        dst.Update()
        self.ref_vtu = dst.GetOutput()
        self.ref_vtu_dsa = dsa.WrapDataObject(self.ref_vtu)

    def test_get_nc_data(self):

        l = n2v.get_nc_data(self.dataset, self.nc_data_var)

        isinstance(l, list)
        assert len(l) == 2
        isinstance(l[0], tuple)
        isinstance(l[1], tuple)
        assert l[0][0] == "SWC_L01"
        assert l[1][0] == "SWC_L02"
        assert l[0][1].shape == (2,27,21)
        assert l[1][1].shape == (2,27,21)

        # assert data
        assert_array_almost_equal(l[0][1][0], self.swcl01[0])
        assert_array_almost_equal(l[0][1][1], self.swcl01[1])
        assert_array_almost_equal(l[1][1][0], self.swcl02[0])
        assert_array_almost_equal(l[1][1][1], self.swcl02[1])


    def test_create_vtp_and_nc_data_to_vtp(self):

        ref_vtp_dsa = self.ref_vtp_dsa
        ref_vtp_points = ref_vtp_dsa.Points

        vtp = n2v.create_vtp(self.lon_dat, self.lat_dat, self.nc_crs, self.vtu_crs)

        isinstance(vtp, vtkPolyData)

        vtp_dsa = dsa.WrapDataObject(vtp)
        vtp_points = vtp_dsa.Points

        # compare coordinate points
        assert_array_almost_equal(
            array(vtp_points),
            array(ref_vtp_points))


    def test_nc_data_to_vtp(self):

        ref_vtp_dsa = self.ref_vtp_dsa

        # create vtp and add data
        vtp = n2v.create_vtp(self.lon_dat, self.lat_dat, self.nc_crs, self.vtu_crs)

        l = [("SWC_L01", self.swcl01),
             ("SWC_L02", self.swcl02)]
        n2v.nc_data_to_vtp(vtp, l, self.time_dat)

        vtp_dsa = dsa.WrapDataObject(vtp)

        # compare data with ref_vtp_dsa
        assert ref_vtp_dsa.PointData.keys() == vtp_dsa.PointData.keys()

        assert_array_almost_equal(
            ref_vtp_dsa.PointData.GetArray(0),
            vtp_dsa.PointData.GetArray(0))

        assert_array_almost_equal(
            ref_vtp_dsa.PointData.GetArray(1),
            vtp_dsa.PointData.GetArray(1))

        assert_array_almost_equal(
            ref_vtp_dsa.PointData.GetArray(2),
            vtp_dsa.PointData.GetArray(2))

        assert_array_almost_equal(
            ref_vtp_dsa.PointData.GetArray(3),
            vtp_dsa.PointData.GetArray(3))


    def test_interpolate_vtp_data_on_vtu(self):

        ref_vtu_dsa = self.ref_vtu_dsa

         # create vtp and add data
        vtp = n2v.create_vtp(self.lon_dat, self.lat_dat, self.nc_crs, self.vtu_crs)

        l = [("SWC_L01", self.swcl01),
             ("SWC_L02", self.swcl02)]
        n2v.nc_data_to_vtp(vtp, l, self.time_dat)

        # read vtu
        vtu = n2v.read_vtu(self.vtu_in)

        # interpolate
        out_vtu = n2v.interpolate_vtp_data_on_vtu(vtp, vtu, self.map_func_type, self.nullval)
        out_vtu_dsa = dsa.WrapDataObject(out_vtu)

        # compare out_vtu with ref_vtu
        # compare coordinate points
        assert_array_almost_equal(
            array(ref_vtu_dsa.Points),
            array(out_vtu_dsa.Points))
        # compare data
        assert ref_vtu_dsa.PointData.keys() == out_vtu_dsa.PointData.keys()

        assert_array_almost_equal(
            ref_vtu_dsa.PointData.GetArray(0),
            out_vtu_dsa.PointData.GetArray(0))

        assert_array_almost_equal(
            ref_vtu_dsa.PointData.GetArray(1),
            out_vtu_dsa.PointData.GetArray(1))

        assert_array_almost_equal(
            ref_vtu_dsa.PointData.GetArray(2),
            out_vtu_dsa.PointData.GetArray(2))

        assert_array_almost_equal(
            ref_vtu_dsa.PointData.GetArray(3),
            out_vtu_dsa.PointData.GetArray(3))


    def test_read_vtu(self):

        vtu = n2v.read_vtu(self.vtu_ref_path)
        isinstance(vtu, vtkUnstructuredGrid)


    def test_write_vtu(self, tmp_path):

        file = str(tmp_path/self.vtu_out)
        n2v.write_vtu(self.ref_vtu, file)
        os.path.isfile(file)
        # reload and test
        vtu = n2v.read_vtu(self.vtu_ref_path)
        isinstance(vtu, vtkUnstructuredGrid)


    def test_write_vtp(self, tmp_path):

        file = str(tmp_path/self.vtp_out)
        n2v.write_vtp(self.ref_vtp, file)
        os.path.isfile(file)
        # reload and test
        rdr = vtk.vtkXMLPolyDataReader()
        rdr.SetFileName(file)
        rdr.Update()
        vtp = rdr.GetOutput()
        isinstance(vtp, vtkPolyData)


    def test_set_map_function(self):

        map_fun1 = n2v.set_map_function(1)
        map_fun2 = n2v.set_map_function(2)
        map_fun3 = n2v.set_map_function(3)

        isinstance(map_fun1, vtkVoronoiKernel)
        isinstance(map_fun2, vtkGaussianKernel)
        isinstance(map_fun3, vtkShepardKernel)


class TestCli():

    def setup_method(self):
        # def command for cli
        self.com = ['netcdf2vtu', '-o', out_vtu_path_cli,
                    '-m', str(map_func_type), '-n', str(nullvalue),
                    '--lat', coordnames[0], '--lon', coordnames[1],
                    '--time', coordnames[2],
                    nc_file1, in_vtu_path, nc_crs, vtu_crs,
                    data_var_names[0]]


    def test_successful_exec(self, tmp_path):

        com = self.com[:]
        file = str(tmp_path/out_vtu_path_cli)
        com[2] = file
        result = subprocess.run(com, stdout=subprocess.PIPE)
        assert result.returncode == 0
        assert os.path.isfile(file)


    def test_missing_required_args(self):

        with raises(subprocess.CalledProcessError):
            subprocess.run(["netcdf2vtu"], stdout=subprocess.PIPE,
            check=True)


    def test_default_vals(self):

        com = self.com[:1]+self.com[11:]
        result = subprocess.run(com, stdout=subprocess.PIPE)
        assert result.returncode == 0
        assert os.path.isfile("out.vtu")
        os.remove("out.vtu")



    def test_invalid_arg_vals(self):

        com = self.com[:1]+["-m", "X"]+self.com[11:]
        with raises(subprocess.CalledProcessError):
            subprocess.run(com, stdout=subprocess.PIPE, check=True)


    def test_opt_args_not_given(self, tmp_path):

        com = self.com[:]
        file = str(tmp_path/"5_")+out_vtu_path_cli
        com[2] = file
        com.pop(11)
        com.pop(11)
        result = subprocess.run(com, stdout=subprocess.PIPE)
        assert result.returncode == 0
        assert os.path.isfile(file)

