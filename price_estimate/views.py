import json

from django.shortcuts import render
from django.views.generic import View

from price_estimate import data_processing as dp
import pandas as pd


class PriceEstimateView(View):
    def get(self, request):
        data = request.GET

        # In dữ liệu người dùng nhập ra console
        print(json.dumps(data, indent=4, ensure_ascii=False))

        # Có thể lấy dữ liệu người dùng nhập từ biến `data` giống như 1 dictionary
        # VD: lấy name, phone, email thì làm như sau:
        # name = data.get('name')
        # phone = data.get('phone')
        # email = data.get('email')

        # NaN = float("NaN")
        # Setting data
        # record_data = [
        #     [17.0, 39, NaN, 132.0, 22.0, 6.0, NaN, NaN, NaN, NaN, NaN, NaN, 15.0, NaN, NaN, NaN, NaN, NaN, NaN, NaN,
        #      True, True, True, True, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN,
        #      NaN, NaN, NaN, NaN]]
        # record = pd.DataFrame(record_data,
        #                       columns=['FormRE', 'Province', 'FloorNum', 'Area', 'Height', 'Width', 'UsableArea',
        #                                'FrontLength', 'BackSideLength', 'Direction', 'BalconyDirection', 'Corner',
        #                                'RoadInFront', 'Juridical', 'NumOfBed', 'NumOfFloor', 'NumOfToilet',
        #                                'ConstructionYear',
        #                                'IsOwner', 'Furniture', 'Terrace', 'CarParking', 'DinningRoom', 'Kitchen',
        #                                'AirCond', 'ADSL', 'WashingMachine', 'Balcony', 'Fridge', 'Wifi', 'Pool',
        #                                'Basement', 'Park', 'SuperMarket', 'Clinics', 'Sea', 'Hospital', 'Church',
        #                                'BusStation', 'School', 'Temple', 'Airport', 'Preschool', 'Characteristics'])

        # print("test: ", data.get('real_estate_form').var('option'))
        # print(data.get('real_estate_form'))
        # print("real_estate_form: ", data.get('real_estate_form'))

        # Imputing missing values
        # record = dp.vn_imputing_missing_values(record)
        #
        # record = dp.vn_record_load_transform_numerical_to_categorical_values(record)
        #
        # record = dp.box_cox_transform_skewed_features_loaded(record)
        #
        # print("Type of record: ", type(record))
        # # Getting new record
        # print(record.shape)
        #
        # dp_record = pd.get_dummies(record)

        # PREDICTING ############
        # from price_estimate import modelling as mlg

        # Load trained models
        # trained_model_xgb, trained_model_lgb, trained_stacked_averaged_models = mlg.load_models()

        # Predict
        # out = mlg.run_predict_models(trained_stacked_averaged_models, trained_model_xgb, trained_model_lgb, record)

        # Sau khi tính toán, cập nhật context['estimation'] và context['estimation_text'] bên dưới
        # thì màn hình sẽ tự hiển thị phần "Kết quả định giá"
        # VD:
        # context['estimation'] = '123 tỷ'
        # context['estimation_text'] = 'Một trăm hai mươi ba tỷ'
        context = {}
        context['estimation'] = ''
        context['estimation_text'] = ''

        return render(request, 'price_estimate/index.html', context)

    def post(self, request):
        data = request.POST

        # In dữ liệu người dùng nhập ra console
        print(json.dumps(data, indent=4, ensure_ascii=False))

        # Có thể lấy dữ liệu người dùng nhập từ biến `data` giống như 1 dictionary
        # VD: lấy name, phone, email thì làm như sau:
        # name = data.get('name')
        # phone = data.get('phone')
        # email = data.get('email')

        NaN = float("NaN")
        # Setting data
        floor_no = data.get('floor_no') if data.get('floor_no') != '' else NaN
        use_area = float(data.get('use_area')) if data.get('use_area') != '' else NaN
        front_length = float(data.get('front_length')) if data.get('front_length') != '' else NaN
        back_length = float(data.get('back_length')) if data.get('back_length') != '' else NaN
        house_direction = data.get('house_direction') if data.get('house_direction') != '0' else NaN
        balcony_direction = data.get('balcony_direction') if data.get('balcony_direction') != '0' else NaN
        corner_unit = False if data.get('corner_unit') != 1 else True
        distance_house_to_way = float(data.get('distance_house_to_way')) if data.get('distance_house_to_way') != '' else NaN
        # Juridical
        bedroom_number = float(data.get('bedroom_number')) if data.get('bedroom_number') != '' else NaN
        floor_number = float(data.get('floor_number')) if data.get('floor_number') != '' else NaN
        # NumOfToilet
        # ConstructionYear
        # IsOwner
        # Furniture
        # Terrace: True
        # CarParking: True
        # DinningRoom: True
        # Kitchen: True
        # AirCond
        # ADSL
        # WashingMachine
        # Balcony
        # Fridge
        # Wifi
        # Pool
        # Basement
        # Park
        # SuperMarket
        # Clinics
        # Sea
        # Hospital
        # Church
        # BusStation
        # School
        # Temple
        # Airport
        # Preschool
        house_feature = data.get('house_feature') if data.get('house_feature') != '0' else NaN  # Characteristics

        # print("area: ", data.get('area'))
        record_data = [
            [data.get('real_estate_form'), data.get('city_address'), NaN, float(data.get('area')),
             float(data.get('length')),
             float(data.get('width')), use_area, front_length, back_length, house_direction, NaN, NaN,
             distance_house_to_way, NaN, bedroom_number, floor_number, NaN, NaN, NaN, NaN,
             True, True, True, True, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN,
             NaN, NaN, NaN, NaN]]
        record = pd.DataFrame(record_data,
                              columns=['FormRE', 'Province', 'FloorNum', 'Area', 'Height', 'Width', 'UsableArea',
                                       'FrontLength', 'BackSideLength', 'Direction', 'BalconyDirection', 'Corner',
                                       'RoadInFront', 'Juridical', 'NumOfBed', 'NumOfFloor', 'NumOfToilet',
                                       'ConstructionYear',
                                       'IsOwner', 'Furniture', 'Terrace', 'CarParking', 'DinningRoom', 'Kitchen',
                                       'AirCond', 'ADSL', 'WashingMachine', 'Balcony', 'Fridge', 'Wifi', 'Pool',
                                       'Basement', 'Park', 'SuperMarket', 'Clinics', 'Sea', 'Hospital', 'Church',
                                       'BusStation', 'School', 'Temple', 'Airport', 'Preschool', 'Characteristics'])

        # print("test: ", data.get('real_estate_form').var('option'))
        # print(data.get('real_estate_form'))

        # Imputing missing values
        record = dp.vn_imputing_missing_values(record)

        record = dp.vn_record_load_transform_numerical_to_categorical_values(record)

        record = dp.box_cox_transform_skewed_features_loaded(record)

        print("Type of record: ", type(record))
        # Getting new record
        print(record.shape)

        dp_record = pd.get_dummies(record)

        # PREDICTING ############
        from price_estimate import modelling as mlg

        # Load trained models
        trained_model_xgb, trained_model_lgb, trained_stacked_averaged_models = mlg.load_models()

        # Predict
        out = mlg.run_predict_models(trained_stacked_averaged_models, trained_model_xgb, trained_model_lgb, record)

        # Sau khi tính toán, cập nhật context['estimation'] và context['estimation_text'] bên dưới
        # thì màn hình sẽ tự hiển thị phần "Kết quả định giá"
        # VD:
        # context['estimation'] = '123 tỷ'
        # context['estimation_text'] = 'Một trăm hai mươi ba tỷ'
        context = {}
        context['estimation'] = out
        import math
        context['estimation_text'] = str(round(float(out/1000000000), 2)) + ' Tỷ VND'

        return render(request, 'price_estimate/index.html', context)

