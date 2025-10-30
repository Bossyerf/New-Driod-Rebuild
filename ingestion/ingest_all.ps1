param()
$ErrorActionPreference = 'Stop'
Write-Host "Ingesting UE docs and E:\\UeSource (placeholders)..."
python ingestion/ingest_docs.py
python ingestion/ingest_ue_source.py
Write-Host "Done."
exit 0
