% Basic integrate-and-fire neuron 
% R Rao 2007
% with added noise

clear

% capacitance and leak resistance
C = 1 % nF
R = 40 % M ohms

% I & F implementation dV/dt = - V/RC + I/C
% Using h = 1 ms step size, Euler method

V = 0;
tstop = 200; % total integration time
abs_ref = 5; % absolute refractory period 
ref = 0; % absolute refractory period counter
V_trace = []; % voltage trace for plotting
V_th = 10; % spike threshold
spiketimes = []; % list of spike times

% input current
noiseamp = 0;   % amplitude of added noise
I = 1 + noiseamp*randn(1,tstop); % nA; Gaussian noise


for t = 1:tstop
  
   if ~ref
     V = V - (V/(R*C)) + (I(t)/C)
   else
     ref = ref - 1;
     V = 0.2*V_th; % reset voltage
   end
   
   if (V > V_th)
     V = 50;  % emit spike
     spiketimes = [spiketimes t]; % save times of spikes 
     ref = abs_ref; % set refractory counter
   end

   V_trace = [V_trace V];

end

  plot(V_trace)

