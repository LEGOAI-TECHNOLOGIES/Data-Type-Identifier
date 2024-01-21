from legoai.pipeline import DataTypeIdentificationPipeline
from legoai.core.model_configuration import MODEL_CONFIG

if __name__ == "__main__":
    
       
        dataset_name = "ecommerce_data"
    
        di_pipeline = DataTypeIdentificationPipeline(dataset_name=dataset_name,open_api_key= MODEL_CONFIG["L3PARAMS"]["OPENAI_API_KEY"])
        # # prediction = DataTypeIdentificationPipeline.load_default_model(open_api_key="")
        prediction = di_pipeline.run_pipeline(save_result=False)
        print(prediction[['column_name_clean','predicted_datatype_l1','predicted_datatype_l3']].head())