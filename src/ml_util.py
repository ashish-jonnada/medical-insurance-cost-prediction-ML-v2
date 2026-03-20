from sklearn.linear_model import LinearRegression,Ridge,Lasso

def encode_binary(df,column):
    df[column] = df[column].map({"yes":1,"no":0})
    return df

def train_model(X,y,model_type="linear"):
    if model_type == "linear":
        model = LinearRegression()
    elif model_type == "ridge":
        model = Ridge()
    elif model_type == "lasso":
        model = Lasso()
    else:
        raise ValueError("Unsupported model type")
    
    model.fit(X,y)
    return model 