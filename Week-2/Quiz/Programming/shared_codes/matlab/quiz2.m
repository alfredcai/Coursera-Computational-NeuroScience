close all; 
%clear all; 
clc;
load('c1p8.mat');

% Fill in these values
sampling_period = 2; % in ms
num_timesteps = 150;

sta = compute_sta(stim, rho, num_timesteps);

time = -sampling_period*(num_timesteps-1):sampling_period:0; % in ms

figure(1);
plot(time, sta);
xlabel('Time (ms)');
ylabel('Stimulus');
title('Spike-Triggered Average');
