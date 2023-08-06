cmake_minimum_required(VERSION 3.9)
project(flagsercount_pybind LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/pybind11)

pybind11_add_module(flagsercount_pybind "${CMAKE_CURRENT_SOURCE_DIR}/src/flagser_count_bindings.cpp")

target_include_directories(flagsercount_pybind PRIVATE .)

if(MSVC)
    target_compile_options(flagsercount_pybind PUBLIC $<$<CONFIG:RELEASE>: /Wall /O2>)
    target_compile_options(flagsercount_pybind PUBLIC $<$<CONFIG:DEBUG>:/O1 /DEBUG:FULL /Zi /Zo>)
else()
    target_compile_options(flagsercount_pybind PUBLIC $<$<CONFIG:RELEASE>: -Ofast>)
    target_compile_options(flagsercount_pybind PUBLIC $<$<CONFIG:DEBUG>: -O2 -ggdb -D_GLIBCXX_DEBUG>)
endif()
