try:
    # 🧪 Ask the user for a filename
    filename = input("Enter the filename to read: ")

    # 🖋️ Open and read the file
    with open(filename, "r") as f:
        content = f.read()

    # Modify content (example: make uppercase)
    modified = content.upper()

    # Write to a new file
    with open("newfile.txt", "w") as f:
        f.write(modified)

    print("✅ Done! Modified content written to newfile.txt")

except FileNotFoundError:
    print("❌ Error: File not found.")
except Exception as e:
    print("⚠️ Error:", e)
