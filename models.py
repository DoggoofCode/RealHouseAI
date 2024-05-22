from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


class LinearRegressionModel:
    def __init__(self) -> None:
        self.source = None
        self.model = LinearRegression()

    def add_source(self, X: pd.DataFrame, y: pd.DataFrame) -> None:
        self.source = (X, y)

    def fit(self) -> None:
        self.model.fit(X=self.source[0], y=self.source[1])

    def predict(self, X: pd.DataFrame) -> pd.DataFrame:
        return self.model.predict(X)


def save_model(model: LinearRegressionModel) -> None:
    model_name: str = input("Please enter a name for the model(none for no save): ")
    if model_name != "":
        with open(f"{model_name}.pkl", 'wb') as file:
            pickle.dump(model, file)
        return None


def process_data(path: str) -> pd.DataFrame:
    # Load the FileData
    print("Reading file data from Condo Data...")
    FileData = pd.read_csv(f'{path}')

    # Turn this into a dataframe
    CondoData = pd.DataFrame(FileData)
    CondoData = CondoData.reindex(columns=["Floor Level",
                                           "Transacted Price ($)",
                                           "Area (SQM)",
                                           "Unit Price ($ PSM)",
                                           "Sale Date", ])
    # Simplify names
    CondoData.rename(columns={"Transacted Price ($)": "Price",
                              "Floor Level": "Floor",
                              "Area (SQM)": "Area",
                              "Unit Price ($ PSM)": "UnitPrice",
                              "Sale Date": "SaleYear"
                              },
                     inplace=True)

    """
    Preprocessing for data
    * Add a sale year column
    * Add a floor column
    * Add a price column
    * Add a unit price column
    """

    # Add a sale year column
    CondoData['SaleYear'] = CondoData['SaleYear'].apply(lambda x: int(x.split('-')[1]))
    CondoData['Floor'] = CondoData['Floor'].apply(lambda x: int(x.split(' ')[0]))
    CondoData["Price"] = CondoData["Price"].apply(
        lambda x: int(x.replace(',', '')))
    CondoData["UnitPrice"] = CondoData["UnitPrice"].apply(
        lambda x: int(x.replace(',', '')))

    return CondoData


def create_model__DEPRICATED__() -> None:
    # Process data
    processed_data = process_data("cds.csv")
    X = processed_data[["Floor", "Area", "SaleYear"]]
    y = processed_data["Price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train)

    # Create a Linear Regression model
    model = LinearRegressionModel()
    model.add_source(X_train, y_train)
    model.fit()

    # Calculate the accuracy of the model
    accuracy = model.model.score(X_test, y_test)
    print(f"The accuracy of the model is {accuracy * 100}%")

    save_model(model)
    return None
