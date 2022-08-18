cmake_minimum_required(VERSION 3.22)
project(multiple_reactor)

set(CMAKE_CXX_STANDARD 23)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)

enable_testing()
add_subdirectory(multiple_reactor)