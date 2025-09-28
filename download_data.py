import kagglehub

# Download latest version
path = kagglehub.dataset_download("chetankv/dogs-cats-images")

print("Path to dataset files:", path)