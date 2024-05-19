Climate Analysis of Nepal from 1981 AD to 2019 AD
---------------------------------------------------------------------------------

This is the end to end project of Nepal's climate analysis and temperature forecasting. The model is trained in google colab and deployed using django web framework.

Interval of data collection: Daily basis

No of Districts: 62 (Some districts are not mentioned in the dataset)

It's a time series forecasting activity where the analysis is done for every districts mentioned but the prediction and forecasting of temperature is done for only Kathmandu district.

Dataset_1st:https://opendatanepal.com/dataset/district-wise-daily-climate-data-for-nepal/resource/70da6b2c-d705-4416-9e17-aca24465d865

Dataset_2nd:https://opendatanepal.com/dataset/district-wise-daily-climate-data-for-nepal/resource/a1601f7e-8eb2-4811-b83d-263d181f9abb

Requirements:
-------------
    pip3 install statsmodels
    pip3 install django
    pip3 install dill
    pip3 install numpy
    pip3 install pandas

To run the project, use the command:
------------------------------------

    python manage.py runserver
    
