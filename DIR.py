import os
import re

dir = "C:\\Users\\krish\\OneDrive\\Documents\\Books"

def count_sentences(text):
    """Count sentences in text using regex"""
    if not text.strip():
        return 0
    # Split by sentence-ending punctuation followed by whitespace or end of string
    sentences = re.split(r'[.!?]+\s+|[.!?]+$', text.strip())
    # Filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

def analyze_text_file(file_path):
    """Analyze text files (.txt, .py, etc.)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            char_count = len(text)
            sentence_count = count_sentences(text)
            return char_count, sentence_count
    except UnicodeDecodeError:
        try:
            # Try with different encoding
            with open(file_path, 'r', encoding='latin-1') as file:
                text = file.read()
                char_count = len(text)
                sentence_count = count_sentences(text)
                return char_count, sentence_count
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return 0, 0
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, 0

def get_file_type(filename):
    """Determine file type based on extension"""
    extension = filename.lower().split('.')[-1] if '.' in filename else 'unknown'
    return extension

def analyze_directory(directory_path):
    """Analyze all files in the directory"""
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return
    
    print(f"Analyzing files in: {directory_path}")
    print("=" * 90)
    print(f"{'File Name':<35} {'Type':<8} {'Size (KB)':<12} {'Characters':<12} {'Sentences':<10}")
    print("-" * 90)
    
    files = os.listdir(directory_path)
    total_files = 0
    total_size = 0
    total_chars = 0
    total_sentences = 0
    file_data = []  # Store file data for sorting later
    
    for filename in sorted(files):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            total_files += 1
            
            # Get file size in bytes, convert to KB
            file_size = os.path.getsize(file_path)
            file_size_kb = file_size / 1024
            total_size += file_size
            
            # Get file type
            file_type = get_file_type(filename)
            
            # Analyze file content based on extension
            char_count = 0
            sentence_count = 0
            
            if file_type in ['txt', 'py', 'md', 'csv']:
                char_count, sentence_count = analyze_text_file(file_path)
                total_chars += char_count
                total_sentences += sentence_count
            elif file_type == 'pdf':
                # For PDF files, we'll just show file info without text analysis
                # since we don't have PyPDF2 installed
                char_count = "N/A (PDF)"
                sentence_count = "N/A (PDF)"
            else:
                # For other file types (images, etc.), just show size
                char_count = "N/A"
                sentence_count = "N/A"
            
            # Store file data for later sorting
            file_data.append({
                'filename': filename,
                'file_type': file_type,
                'file_size_kb': file_size_kb,
                'file_size_bytes': file_size,
                'char_count': char_count,
                'sentence_count': sentence_count
            })
            
            # Truncate long filenames for display
            display_name = filename[:32] + "..." if len(filename) > 35 else filename
            
            # Print file details
            print(f"{display_name:<35} {file_type:<8} {file_size_kb:<12.2f} {char_count:<12} {sentence_count:<10}")
    
    # Print summary
    print("-" * 90)
    print(f"Summary:")
    print(f"  Total files: {total_files}")
    print(f"  Total size: {total_size/1024:.2f} KB ({total_size/(1024*1024):.2f} MB)")
    if total_chars > 0:
        print(f"  Total characters (text files): {total_chars:,}")
        print(f"  Total sentences (text files): {total_sentences:,}")
    
    # Show file type breakdown
    file_types = {}
    for filename in files:
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_type = get_file_type(filename)
            file_types[file_type] = file_types.get(file_type, 0) + 1
    
    print(f"\nFile type breakdown:")
    for file_type, count in sorted(file_types.items()):
        print(f"  .{file_type}: {count} files")
    
    # Print files sorted by size (largest first)
    print("\n" + "=" * 90)
    print("FILES SORTED BY SIZE (Largest to Smallest)")
    print("=" * 90)
    print(f"{'File Name':<35} {'Type':<8} {'Size (KB)':<12} {'Characters':<12} {'Sentences':<10}")
    print("-" * 90)
    
 
    
    for file_info in file_data:
        display_name = file_info['filename'][:32] + "..." if len(file_info['filename']) > 35 else file_info['filename']
        print(f"{display_name:<35} {file_info['file_type']:<8} {file_info['file_size_kb']:<12.2f} {file_info['char_count']:<12} {file_info['sentence_count']:<10}")
    
    return file_data

# Run the analysis
if __name__ == "__main__":
    analyze_directory(dir)
