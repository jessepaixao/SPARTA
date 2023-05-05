close all
clear all
clc

% Post-processing data modal analysis
% ---------------------------------------
% PAIXAO J.  Mar 23


%% IMPORT EXPERIMENTAL DATA

% Read UNV files
file_name={'16_09_22_AIRPLANE_SC_PZT12','16_09_22_AIRPLANE_OC_PZT12'}
folder_data='../data_experiments/'

init_n_frf=5; % Depend on data structure
select_FRF_point=9; % Point to be observed
f_init=10;
f_max=500;
    
line_type={':','-'}
color_line={'k','b'}
for j=1:length(file_name)
    [DS, Info, errmsg] = readuff(strcat(folder_data,file_name{j},'.unv'));

    % Frequency vector
    [i_aux,j_aux]=find(DS{1, init_n_frf}.x(DS{1, init_n_frf}.x>=f_init & DS{1, init_n_frf}.x<=f_max));
    f=transpose(DS{1, init_n_frf}.x(j_aux));

    aux=0;
    for i=init_n_frf:length(DS)
       aux=aux+1;
       H(:,aux)=transpose(DS{1, i}.measData(j_aux));
    end


    x=DS{1, 3}.x;
    y=DS{1, 3}.y;

    
    figure(1)
    plot(x,y,'bo');hold on
    plot(x(select_FRF_point,1),y(select_FRF_point,1),'ro')

    figure(2)
    set(gcf, 'Units', 'Normalized', 'OuterPosition', [0,0,1,1])
    semilogy(f,2*pi*f.*abs(H(:,select_FRF_point)),line_type{j},'linewidth',1.5,'color',color_line{j}); hold on
    xlabel('Frequency [Hz]','interpreter','latex'); 
    ylabel('$H(\omega)$[m/s/N]','interpreter','latex');
    set(gca,'FontSize',24,'TickLabelInterpreter','latex')
    xlim([10 120])
    ylim([1e-4 100])
    
end
legend('Short-circuit','Open-circuit','interpreter','latex',...
    'location','southeast')