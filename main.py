import os

# Đường dẫn thư mục .cache trong thư mục home của người dùng
cache_dir = os.path.join(os.path.expanduser("~"), ".cache")

# Đường dẫn đến thư mục face-parsing trong thư mục .cache
dest_dir = os.path.join(cache_dir, "face-parsing")

# URL của kho lưu trữ cần clone
repo_url = "https://huggingface.co/jonathandinu/face-parsing"

# Tạo thư mục .cache nếu nó chưa tồn tại
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# Clone repository vào thư mục .cache/face-parsing
os.system(f"git clone {repo_url} {dest_dir}")

print(f"Repository đã được clone thành công vào {dest_dir}!")
