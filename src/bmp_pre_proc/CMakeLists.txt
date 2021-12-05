cmake_minimum_required(VERSION 3.10)
project(anti_noise)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS -Ofast)

add_subdirectory(lib)
add_executable(demo driver/cpp/main.cpp)
target_link_libraries(demo PUBLIC _anti_noise)

target_include_directories(demo PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/lib"
                          )

add_library(anti_noise SHARED lib/proc.cpp)