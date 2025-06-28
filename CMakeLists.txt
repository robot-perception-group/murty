cmake_minimum_required(VERSION 3.15)
project(murty VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find required packages
find_package(Python REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

# Create the pybind11 module
pybind11_add_module(_murty cpp/murty.cpp)

# Include directories
target_include_directories(_murty PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/cpp)

# Link libraries
target_link_libraries(_murty PRIVATE Eigen3::Eigen)

# Set properties
set_target_properties(_murty PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED ON
    # Ensure the module name is exactly _murty without any prefix
    OUTPUT_NAME "_murty"
    PREFIX ""
)

# Set the output directory to the package source directory  
set_target_properties(_murty PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src/murty
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src/murty
    LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/src/murty
    RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/src/murty
)

# Compiler-specific options
target_compile_definitions(_murty PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})

# For Windows MSVC
if(MSVC)
    target_compile_options(_murty PRIVATE /W4)
else()
    target_compile_options(_murty PRIVATE -Wall -Wextra -Wpedantic)
endif()

# Install the module to the package directory
install(TARGETS _murty DESTINATION src/murty)