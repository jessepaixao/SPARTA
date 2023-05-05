close all
clear all
clc

% Post-processing data modal analysis
% ---------------------------------------
% PAIXAO J.  Mar 23

%% Set up the Import Options and import the data

file_path="..\data_experiments\21_02_23_INDUCTOR8_CHAR.xlsx"

opts = spreadsheetImportOptions("NumVariables", 7);

% Specify sheet
opts.Sheet = "Sheet1";

% Specify column names and types
opts.VariableNames = ["Voltage", "Var2", "Var3", "Var4", "Var5", "Var6", "InductanceAver"];
opts.SelectedVariableNames = ["Voltage", "InductanceAver"];
opts.VariableTypes = ["double", "char", "char", "char", "char", "char", "double"];

% Specify variable properties
opts = setvaropts(opts, ["Var2", "Var3", "Var4", "Var5", "Var6"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Var2", "Var3", "Var4", "Var5", "Var6"], "EmptyFieldRule", "auto");

% Import the data
data={};
ranges = ["A3:G13", "A17:G27", "A31:G41"];
for idx = 1:length(ranges)
    opts.DataRange = ranges(idx);
    tb = readtable(file_path, opts, "UseExcel", false);
    data{idx} = table2array(tb); 
end



%% PLOT DATA

marker_type={'o--k','o-k','o:k'}
color={'k','k','k'}
figure(1)
for i=1:length(data)
    plot(data{i}(:,1),data{i}(:,2),marker_type{i},'MarkerFaceColor',color{i},'linewidth',1.5); hold on
end

xlabel('Applied Voltage [V]','interpreter','latex'); 
ylabel('Inductance [H]','interpreter','latex');
set(gca,'FontSize',17,'TickLabelInterpreter','latex')
% saveas(gcf, '../paper/figures/inductance_voltage', 'png')

%% PLOT DATA ZOOM

% marker_type={'o--b','o-r','o:k'}
% color={'b','r','k'}
figure(1)
for i=1:length(data)
    plot(data{i}(:,1),data{i}(:,2),marker_type{i},'MarkerFaceColor',color{i},'linewidth',1.5); hold on
end

xlabel('Applied Voltage [V]','interpreter','latex'); 
ylabel('Inductance [H]','interpreter','latex');
xlim([1.95,2.05])
set(gca,'FontSize',17,'TickLabelInterpreter','latex')
% saveas(gcf, '../paper/figures/inductance_voltage_zoom', 'png')



