from django.shortcuts import render
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.pipeline import Pipeline
import __main__
__main__.pd = pd
import dill


# Create your views here.


def feature_entry(request):
    if request.method == 'POST':
                # Retrieve form data
        date = request.POST.get('DATE')


        

        forecast_date = date
        forecast_date=pd.Timestamp(forecast_date)

        with open('analysis/Model/exp_model.pkl', 'rb') as f:
            model = dill.load(f)
        y_pred = model.predict(forecast_date)
        print(y_pred)
        return render(request,'analysis/result.html',{'y_pred':round(y_pred[0],2)})
    return render(request, 'analysis/feature_entry.html')

#  <=============================== YOU CAN IGNORE THE BELOW COMMENTED CODE ==================================>

        # with open('analysis/climate_pipe.pkl','rb')as f:
        #     pipe=dill.load(f)
        #     print('Pipe loaded')

        # district_name = request.POST.get('DISTRICT')
        # ps = float(request.POST.get('PS'))
        # qv2m = float(request.POST.get('QV2M'))
        # ws10m = float(request.POST.get('WS10M'))

        # Construct a dictionary with the input features
        # input_data = {
            # 'DATE': date,
            # 'DISTRICT':district_name,
            # 'PS': ps,
            # 'QV2M': qv2m,
            # 'WS10M':ws10m

        # }
        # input_df = pd.DataFrame(input_data,index=[0])


        # input_df=np.array(input_df)
        # input_df = pipe.transform(input_df)
        # print('Transformed data:',transformed_data)

    
   