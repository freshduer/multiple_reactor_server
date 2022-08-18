aux_source_directory(./src CPP_LIST)

add_executable(server server.cpp ${CPP_LIST})
target_link_libraries(server CONAN_PKG::glog CONAN_PKG::abseil)

add_executable(client client.cpp src/util.cpp src/Buffer.cpp src/Socket.cpp)
target_link_libraries(client CONAN_PKG::glog CONAN_PKG::abseil)

add_executable(ThreadPoolTest src/ThreadPool.cpp ThreadPoolTest.cpp)
target_link_libraries(ThreadPoolTest CONAN_PKG::glog CONAN_PKG::abseil)

add_executable(test1 src/util.cpp src/Buffer.cpp src/Socket.cpp src/ThreadPool.cpp test.cpp)
target_link_libraries(test1 CONAN_PKG::glog CONAN_PKG::abseil)
