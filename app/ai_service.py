def analyze_business_problem(problem: str):
    problem = problem.lower()

    analysis = []

    if "sales" in problem:
        analysis.append("📈 Sales: Review your sales process and identify where customers are dropping off.")

    if "marketing" in problem:
        analysis.append("📢 Marketing: Improve digital marketing, SEO, and social media campaigns.")

    if "customer" in problem:
        analysis.append("👥 Customer Service: Reduce response times and improve customer satisfaction.")

    if "finance" in problem or "money" in problem or "cost" in problem:
        analysis.append("💰 Finance: Reduce unnecessary expenses and improve cash flow.")

    if "employee" in problem or "staff" in problem:
        analysis.append("🏢 Human Resources: Invest in employee training and performance management.")

    if "competition" in problem or "competitor" in problem:
        analysis.append("⚔️ Competition: Analyze competitors and create a stronger value proposition.")

    if not analysis:
        analysis.append("🚀 Overall Recommendation: Gather more business data before making strategic decisions.")

    return {
    "business_problem": problem,
    "executive_summary": "Falcon AI analyzed the business problem and generated strategic recommendations.",

    "recommendations": analysis,

    "strengths": [
        "Business is actively seeking improvement",
        "Management is using AI for decision making"
    ],

    "weaknesses": [
        "Current issue requires attention",
        "Limited business information available"
    ],

    "opportunities": [
        "Increase efficiency",
        "Improve customer satisfaction",
        "Expand market reach"
    ],

    "risks": [
        "Revenue may continue declining",
        "Competitors may gain market share"
    ],

    "priority": "High",

    "action_plan": [
        "Week 1: Collect business performance data.",
        "Week 2: Implement Falcon AI recommendations.",
        "Week 3: Measure results and adjust strategy.",
        "Week 4: Review progress and plan next actions."
    ]
} 