close all
clear all
clc

% SDOF Analysis
% ---------------------------------------
% PAIXAO J.  Mar 23

%% PARAMETERS DEFINITION
m=0.5;
Koc=70000;
c=0.3;
L=106;
R=3050;
Ce=268e-9;
gamma=7.55e-3;
alpha=gamma/Ce;


wn_oc=sqrt(Koc/m);
wn_sc=sqrt((Koc-alpha^2*Ce)/m);

kc=sqrt((wn_oc^2-wn_sc^2)/wn_sc^2);

L=1/(Ce*wn_oc^2);  
R=sqrt(3/2)*kc/(Ce*wn_oc);

we=sqrt(1/(Ce*L))/(2*pi);

%% PLOT

freq=0:0.01:100;
omega=2*pi.*freq;

H_oc=zeros(length(omega),1);
H_ep=zeros(length(omega),1);
H_ep_R1=zeros(length(omega),1);
H_ep_R2=zeros(length(omega),1);
H_adp=zeros(length(omega),1);

R_mod1=0.1*R;
R_mod2=0.1*R;
L_mod=1*L;
R_adp=0.1*R;
% L=1
% L=200
for i = 1:length(omega)
    
    % Open-circuit
    H_oc(i)=1/(-omega(i)^2*m+1j*omega(i)*c+Koc);

    % Equal-peak solution
    H_ep(i)=(-omega(i)^2*L+1j*omega(i)*R+1/Ce)/((-omega(i)^2*m+1j*omega(i)*c+Koc)*(-omega(i)^2*L+1j*omega(i)*R+1/Ce)-alpha^2);
    
    % Equal-peak with 0.1*R
    H_ep_R1(i)=(-omega(i)^2*L_mod+1j*omega(i)*R_mod1+1/Ce)/((-omega(i)^2*m+1j*omega(i)*c+Koc)*(-omega(i)^2*L_mod+1j*omega(i)*R_mod1+1/Ce)-alpha^2);
    H_ep_R2(i)=(-omega(i)^2*L+1j*omega(i)*R_mod2+1/Ce)/((-omega(i)^2*m+1j*omega(i)*c+Koc)*(-omega(i)^2*L+1j*omega(i)*R_mod2+1/Ce)-alpha^2);

    % Adaptive system
    L_adp=1/(Ce*omega(i)^2); 
    H_adp(i)=(-omega(i)^2*L_adp+1j*omega(i)*R_adp+1/Ce)/((-omega(i)^2*m+1j*omega(i)*c+Koc)*(-omega(i)^2*L_adp+1j*omega(i)*R_adp+1/Ce)-alpha^2);
  
end

figure(1)
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0.3, 0.2, 0.4, 0.7])
semilogy(freq/(wn_oc/2/pi),(abs(H_oc)),'linewidth',1.5); hold on
semilogy(freq/(wn_oc/2/pi),(abs(H_ep)),'linewidth',1.5); hold on
semilogy(freq/(wn_oc/2/pi),(abs(H_ep_R1)),'linewidth',1.5); hold on
% semilogy(freq/(wn_oc/2/pi),(abs(H_ep_R2)),'linewidth',1.5); hold on
semilogy(freq/(wn_oc/2/pi),(abs(H_adp)),'linewidth',1.5); hold on
xlim([0.85,1.15])
ylim([1e-5,1e-2])
xlabel('Frequency [Hz]','interpreter','latex'); 
ylabel('$H(\omega)$[m/N]','interpreter','latex');
set(gca,'FontSize',17,'TickLabelInterpreter','latex')
% exportgraphics(gcf, '../paper/figures/frf_sdof.png','Resolution',300)

legend('PVA Off','L=$L_{ep}$ and R=$R_{ep}$ (Equal-peak)','L=$L_{ep}$ and R=$0.1R_{ep}$ (Low Resistance)','L=$L_{adpt}$ and R=$0.1R_{ep}$ (Adaptive)','interpreter','latex','location','northoutside')