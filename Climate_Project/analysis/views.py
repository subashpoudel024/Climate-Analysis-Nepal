from django.shortcuts import render
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.pipeline import Pipeline
import __main__
__main__.pd = pd


# from .forms import FeatureEntryForm

# Create your views here.
import dill
def predict(request):
  pass
        
def welcome(request):
    message = 'Hello'
    return render(request,'analysis/feature_entry.html',{'message':message})


def feature_entry(request):
    if request.method == 'POST':
                # Retrieve form data
        date = request.POST.get('DATE')
        district_name = request.POST.get('DISTRICT')
        latitude = float(request.POST.get('LAT'))
        longitude = float(request.POST.get('LON'))
        ps = float(request.POST.get('PS'))
        qv2m = float(request.POST.get('QV2M'))
        rh2m = float(request.POST.get('RH2M'))
        t2m = float(request.POST.get('T2M'))
        t2mwet = float(request.POST.get('T2MWET'))
        t2m_max = float(request.POST.get('T2M_MAX'))
        t2m_min = float(request.POST.get('T2M_MIN'))
        t2m_range = float(request.POST.get('T2M_RANGE'))
        ws10m = float(request.POST.get('WS10M'))
        ws10m_max = float(request.POST.get('WS10M_MAX'))
        ws10m_min = float(request.POST.get('WS10M_MIN'))
        ws10m_range = float(request.POST.get('WS10M_RANGE'))
        ws50m = float(request.POST.get('WS50M'))
        ws50m_max = float(request.POST.get('WS50M_MAX'))
        ws50m_min = float(request.POST.get('WS50M_MIN'))
        ws50m_range = float(request.POST.get('WS50M_RANGE'))

        with open('analysis/climate_pipe.pkl','rb')as f:
            pipe=dill.load(f)
            print('Pipe loaded')
        
        # Construct a dictionary with the input features
        input_data = {
            'DATE': date,
            'DISTRICT':district_name,
            'LAT': latitude,
            'LON':longitude,
            'PS': ps,
            'QV2M': qv2m,
            'RH2M':rh2m,
            'T2M': t2m,
            'T2MWET': t2mwet,
            'T2M_MAX': t2m_max,
            'T2M_MIN': t2m_min,
            'T2M_RANGE': t2m_range,
            'WS10M': ws10m,
            'WS10M_MAX': ws10m_max,
            'WS10M_MIN': ws10m_min,
            'WS10M_RANGE': ws10m_range,
            'WS50M': ws50m,
            'WS50M_MAX': ws50m_max,
            'WS50M_MIN': ws50m_min,
            'WS50M_RANGE': ws50m_range
        }
        
        input_df = pd.DataFrame(input_data,index=[0])


        # input_df=np.array(input_df)
        input_df = pipe.transform(input_df)
        # print('Transformed data:',transformed_data)

        with open('analysis/climate_model_xgb.pkl', 'rb') as f:
            model = dill.load(f)
        input_df = xgb.DMatrix(input_df)
        y_pred = model.predict(input_df)
        print(y_pred)
        return render(request,'analysis/result.html',{'y_pred':y_pred})

    
   
    return render(request, 'analysis/feature_entry.html')