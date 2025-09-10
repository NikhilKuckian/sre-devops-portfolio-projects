# Git Branching Workflow
## 🚀 Overview
This project documents a **Git workflow** for DevOps teams to collaborate efficiently.  
The strategy prevents broken code from reaching production and ensures proper code review before merge.
## 🔄 Branching Strategy
- **main** → production-ready  
- **dev** → integration branch for testing  
- **feature/** → short-lived branches for new tasks/features  
## 📌 Workflow Example
1. Create feature branch: `feature/log-rotation-enhancement`
2. Commit and push changes
3. Open Pull Request → target `dev`
4. Once validated, merge `dev` → `main`
## 🎯 Benefits
- Prevents breaking `main`
- Enables peer review
- Clear history and traceability
- Fits well with Jenkins/GitHub Actions CI pipelines
## 🧠 Interview Angle
**Q: How do you manage Git workflows in a DevOps team?**  
**A:**
- Use branching model with `main` (prod), `dev` (integration), and `feature/*` (task).  
- Protect `main` branch, require PRs + approvals.  
- Combined with CI/CD, this ensures only tested code reaches production.