from django.shortcuts import render
import pandas as pd
import numpy as np
# import xgboost as xgb
# from sklearn.pipeline import Pipeline
import __main__
__main__.pd = pd
import dill
import prophet

# Create your views here.


def feature_entry(request):
    if request.method == 'POST':
                # Retrieve form data
        date = request.POST.get('DATE')
        ps = float(request.POST.get('PS'))
        qv2m = float(request.POST.get('QV2M'))
        ws10m = float(request.POST.get('WS10M'))

                
        # Initialize a DataFrame with a single row
        future = pd.DataFrame({'ds': [date]})
        # Convert the 'ds' column to datetime
        future['ds'] = pd.to_datetime(future['ds'])

        # Extract year, month, and day from the 'ds' column
        future['YEAR'] = future['ds'].dt.year
        future['MONTH'] = future['ds'].dt.month
        future['DAY'] = future['ds'].dt.day

        # Add other columns with constant values
        future['PS'] = ps
        future['QV2M'] = qv2m
        future['WS10M'] = ws10m


        

        # forecast_date = date
        # forecast_date=pd.Timestamp(forecast_date)

        with open('analysis/Model/fb-prophet_model.pkl', 'rb') as f:
            model = dill.load(f)
        forecast = model.predict(future)

        forecast_final = forecast[['yhat','yhat_lower','yhat_upper']]
        # Rename the columns
        forecast_final.columns = ['Average-Forecast', 'Minimum-Forecast', 'Maximum-Forecast']
        print('Forecast:', forecast_final)
        print(type(forecast_final))

        return render(request,'analysis/result.html',{'avg': round(forecast_final['Average-Forecast'].iloc[0],2),
                                                      'min': round(forecast_final['Minimum-Forecast'].iloc[0],2),
                                                      'max': round(forecast_final['Maximum-Forecast'].iloc[0],2)
                                                      })
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

    
   