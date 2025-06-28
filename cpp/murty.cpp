#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <tuple>
#include <Eigen/Core>
#include "murty.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_murty, m) {
    m.doc() = "Murty's Algorithm implementation for k-best linear assignment problems"; // Add docstring

    py::class_<lap::Murty>(m, "Murty")
        .def(py::init<lap::CostMatrix>(), 
             py::arg("cost_matrix"),
             "Initialize Murty algorithm with a cost matrix")
        .def("draw", &lap::Murty::draw_tuple,
             "Draw the next best assignment\n\n"
             "Returns:\n"
             "    tuple: (success, cost, solution)\n"
             "        - success (bool): True if a solution was found\n"
             "        - cost (float): Cost of the assignment\n"
             "        - solution (np.ndarray): Assignment vector\n");
}
