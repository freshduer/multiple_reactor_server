from conans import ConanFile, CMake


class Conan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "abseil/20211102.0", "glog/0.6.0"
    build_requires = "gtest/1.8.1", "benchmark/1.6.1", "zstd/1.5.2", "boost/1.79.0"  # ,"folly/2020.08.10.00"
    generators = "cmake"
    # Binary configuration
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
