import os
import shutil

def reorganize_folder(old_folder, new_folder):
    # Tạo thư mục mới nếu chưa tồn tại
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    
    # Duyệt qua tất cả các thư mục con trong thư mục gốc
    for subdir, _, files in os.walk(old_folder):
        # Bỏ qua thư mục gốc
        if subdir == old_folder:
            continue
        
        # Lấy ID từ tên thư mục con (ví dụ: '001', '002', ...)
        folder_id = os.path.basename(subdir)
        
        # Duyệt qua tất cả các tệp trong thư mục con
        for file in files:
            # Tạo tên mới cho tệp
            new_filename = f"{folder_id}_{file}"
            # Đường dẫn tệp nguồn
            src_file = os.path.join(subdir, file)
            # Đường dẫn tệp đích
            dest_file = os.path.join(new_folder, new_filename)
            
            # Sao chép tệp từ nguồn đến đích
            shutil.copy(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

# Đường dẫn đến thư mục gốc và mới
old_folder = "data/IrisImage"
new_folder = "data/original_renamed"

# Gọi hàm để tái tổ chức thư mục
reorganize_folder(old_folder, new_folder)
