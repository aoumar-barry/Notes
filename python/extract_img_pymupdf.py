doc = pymupdf.open("file.pdf")

    for page_number in range(len(doc)):
        for img in doc[page_number].get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_storage_path = f"image_{page_number}_{xref}.{image_ext}"
            with open(image_storage_path, "wb") as f:
                f.write(image_bytes)