from pyspark.sql.types import (ArrayType, BinaryType, DoubleType, StructType,
                               StructField, StringType, IntegerType, LongType)

ARCHIVE_ORG_SCHEMA = StructType([
    StructField("created", LongType(), True),
    StructField("d1", StringType(), True),
    StructField("d2", StringType(), True),
    StructField("dir", StringType(), True),
    StructField(
        "files",
        ArrayType(
            StructType([
                StructField("bitrate", StringType(), True),
                StructField("btih", StringType(), True),
                StructField("crc32", StringType(), True),
                StructField("format", StringType(), True),
                StructField("height", StringType(), True),
                StructField("length", StringType(), True),
                StructField("license", StringType(), True),
                StructField("md5", StringType(), True),
                StructField("mtime", StringType(), True),
                StructField("name", StringType(), True),
                StructField("original", StringType(), True),
                StructField("rotation", StringType(), True),
                StructField("sha1", StringType(), True),
                StructField("size", StringType(), True),
                StructField("source", StringType(), True),
                StructField("title", StringType(), True),
                StructField("track", StringType(), True),
                StructField("width", StringType(), True),
                # Strangely, choosing "BooleanType()" for "private" makes all of the rows "null".
                StructField("private", StringType(), True)
            ]), True),
        True),
    StructField("files_count", LongType(), True),
    StructField("identifier", StringType(), True),
    StructField("item_last_updated", LongType(), True),
    StructField("item_size", LongType(), True),
    StructField(
        "metadata",
        StructType([
            StructField("Length", StringType(), True),
            StructField("addeddate", StringType(), True),
            StructField("adder", StringType(), True),
            StructField("aspect_ratio", StringType(), True),
            StructField("backup_location", StringType(), True),
            StructField("closed_captioning", StringType(), True),
            StructField("collection", StringType(), True),
            StructField("color", StringType(), True),
            StructField("contact", StringType(), True),
            StructField("coverage", StringType(), True),
            StructField("creator", StringType(), True),
            StructField("credits", StringType(), True),
            StructField("curation", StringType(), True),
            StructField("date", StringType(), True),
            StructField("description", StringType(), True),
            StructField("director", StringType(), True),
            StructField("duration", StringType(), True),
            StructField("format", StringType(), True),
            StructField("genre", StringType(), True),
            StructField("glob", StringType(), True),
            StructField("holder", StringType(), True),
            StructField("ia_orig__runtime", StringType(), True),
            StructField("identifier", StringType(), True),
            StructField("identifier-access", StringType(), True),
            StructField("identifier-ark", StringType(), True),
            StructField("imdb", StringType(), True),
            StructField("keywords", StringType(), True),
            StructField("language", StringType(), True),
            StructField("lcenseurl", StringType(), True),
            StructField("license", StringType(), True),
            StructField("licenseurl", StringType(), True),
            StructField("licensurl", StringType(), True),
            StructField("mediatype", StringType(), True),
            StructField("noarchivetorrent", StringType(), True),
            StructField("ocr", StringType(), True),
            StructField("omp-locally-produced", StringType(), True),
            StructField("omp-project", StringType(), True),
            StructField("own", StringType(), True),
            StructField("pbcore-genre", StringType(), True),
            StructField("pick", StringType(), True),
            StructField("ppi", StringType(), True),
            StructField("presenter", StringType(), True),
            StructField("producer", StringType(), True),
            StructField("publicdate", StringType(), True),
            StructField("publisher", StringType(), True),
            StructField("release_date", StringType(), True),
            StructField("repub_state", StringType(), True),
            StructField("resource", StringType(), True),
            StructField("runtime", StringType(), True),
            StructField("scanner", StringType(), True),
            StructField("segments", StringType(), True),
            StructField("series", StringType(), True),
            StructField("sound", StringType(), True),
            StructField("sponsor", StringType(), True),
            StructField("subject", StringType(), True),
            StructField("title", StringType(), True),
            StructField("tv-parental-guidelines", StringType(), True),
            StructField("updatedate", StringType(), True),
            StructField("updater", StringType(), True),
            StructField("upload_application", StringType(), True),
            StructField("uploader", StringType(), True),
            StructField("vimeo-height", StringType(), True),
            StructField("vimeo-id", StringType(), True),
            StructField("vimeo-n-entries", StringType(), True),
            StructField("vimeo-playlist", StringType(), True),
            StructField("vimeo-playlist-index", StringType(), True),
            StructField("vimeo-uploader", StringType(), True),
            StructField("vimeo-uploader-id", StringType(), True),
            StructField("vimeo-view-count", StringType(), True),
            StructField("vimeo-webpage-url", StringType(), True),
            StructField("vimeo-width", StringType(), True),
            StructField("year", StringType(), True),
            StructField("youtube-height", StringType(), True),
            StructField("youtube-id", StringType(), True),
            StructField("youtube-n-entries", StringType(), True),
            StructField("youtube-playlist", StringType(), True),
            StructField("youtube-playlist-index", StringType(), True),
            StructField("youtube-uploader", StringType(), True),
            StructField("youtube-uploader-id", StringType(), True),
            StructField("youtube-view-count", StringType(), True),
            StructField("youtube-webpage-url", StringType(), True),
            StructField("youtube-width", StringType(), True)
        ]), True),
])
