import analyze_text as at

src = input("Enter Google Cloud URL of PDF:\n")
dest = input("Enter Google Cloud URL of destination:\n")

output = at.async_detect_document(src, dest)
at.write_to_text(output)


