from fastapi import FastAPI from ai_consultant.strategy_engine import StrategyGenerator from ai_consultant.audit_tool import CapabilityAuditor

app = FastAPI(title="Staqlt AI Consultant Hub") auditor = CapabilityAuditor() strategist = StrategyGenerator()

@app.post("/audit/analyze-capabilities") async def analyze_business(data_source: dict): """ Analyzes current business processes to identify AI integration points. """ analysis = await auditor.run_diagnostic(data_source) return {"status": "Analysis Complete", "findings": analysis}

@app.post("/strategy/generate-roadmap") async def create_roadmap(findings: list): """ Generates a 12-month technical AI implementation roadmap. """ roadmap = await strategist.build_implementation_plan(findings) return {"roadmap": roadmap}

if name == "main": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)