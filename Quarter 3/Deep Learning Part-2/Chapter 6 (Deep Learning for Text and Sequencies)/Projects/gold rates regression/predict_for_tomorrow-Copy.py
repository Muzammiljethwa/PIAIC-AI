def predict_for_tomorrow():
    
    from tensorflow.keras.models import load_model
    from fetch_data import get_latest_data
    import numpy
    import json
    
    model = load_model("Gold_Price_Prediction_Model2.h5")
    data = get_latest_data()
    
    li = []
    for i in data:
        li.append(float(i)/100)
        
    li = numpy.array(li)
    
    def predict_1d(data):
        
        inp = numpy.array(data).reshape((1,5))  
        prediction = model.predict(inp)
        print("Predicted: %s"%(prediction[0][0]*100))
        return float(prediction[0][0]*100)
    
    json_file = open("mean_info.json","r")
    file = json.load(json_file)
    
    mean = numpy.array(file['mean'])
    std = numpy.array(file['std'])
    
    json_file.close()
    
    li -= mean
    li /= std
    
    predicted_data = predict_1d(li)
    return predicted_data
predict_for_tomorrow()