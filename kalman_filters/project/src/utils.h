#ifndef INCLUDE_PROJECT_UTILS_H
#define INCLUDE_PROJECT_UTILS_H

#include "display.h"
#include <vector>

double wrapAngle(double angle);
double mean(const std::vector<double> &dataset);
double RMSE(const std::vector<double> &dataset);
double wrapAngle(double angle);
double calculateMean(const std::vector<double> &dataset);
double calculateRMSE(const std::vector<double> &dataset);

std::vector<Eigen::Vector2d> generateEllipse(double x, double y,
                                             double sigma_xx, double sigma_yy,
                                             double sigma_xy,
                                             int num_points = 50);
std::vector<Eigen::Vector2d> generateCircle(double x, double y, double radius,
                                            int num_points = 50);

#endif // INCLUDE_AKFSFSIM_UTILS_H
