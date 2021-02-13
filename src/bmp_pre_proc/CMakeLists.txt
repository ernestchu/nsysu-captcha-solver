cmake_minimum_required(VERSION 3.18)
project(anti_noise)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS -Ofast)

add_subdirectory(lib)
add_executable(demo driver/cpp/main.cpp)
target_link_libraries(demo PUBLIC anti_noise)

target_include_directories(demo PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/MathFunctions"
                          )