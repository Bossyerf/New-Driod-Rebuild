param()
$ErrorActionPreference = 'Stop'

Write-Host "Starting MCP servers..."
Start-Process powershell -ArgumentList '-NoProfile','-Command','uvicorn mcp.unreal.server:app --host 127.0.0.1 --port 8001' | Out-Null
Start-Process powershell -ArgumentList '-NoProfile','-Command','uvicorn mcp.vision.server:app --host 127.0.0.1 --port 8002' | Out-Null

Write-Host "Run ingestion (placeholders)..."
powershell -NoProfile -Command "python ingestion/ingest_docs.py; python ingestion/ingest_ue_source.py" | Out-Null

Write-Host "Autonomy scaffold is running. In Cursor, enable Parallel/Cloud Agents and set goals."
