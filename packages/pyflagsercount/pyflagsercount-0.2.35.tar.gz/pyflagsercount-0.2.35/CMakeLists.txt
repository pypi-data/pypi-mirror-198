cmake_minimum_required(VERSION 2.8)
project(flagsercount_pybind LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/pybind11)

pybind11_add_module(flagsercount_pybind "${CMAKE_CURRENT_SOURCE_DIR}/src/flagser_count_bindings.cpp")

target_include_directories(flagsercount_pybind PRIVATE .)
