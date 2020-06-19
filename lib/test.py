
from gwpy.timeseries import TimeSeries


start = '2019 Oct 10 05:36:46'
end = '2019 Oct 10 05:46:18'
chname = 'K1:VIS-PRM_IM_DAMP_L_IN1_DQ'
data = TimeSeries.fetch(chname,start,end,host='k1nds0',port=8088)
