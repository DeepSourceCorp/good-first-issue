#!/usr/bin/env python
"""Test script to simulate GitHub Actions workflow locally."""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return success status."""
    print(f"\n🔄 {description}")
    print(f"Running: {cmd}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print("✅ SUCCESS")
            if result.stdout:
                print(result.stdout)
        else:
            print("❌ FAILED")
            if result.stderr:
                print(f"Error: {result.stderr}")
            if result.stdout:
                print(f"Output: {result.stdout}")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")
        return False

def test_workflow_steps():
    """Test all workflow steps locally."""
    print("🧪 Testing GitHub Actions Workflow Locally")
    print("=" * 60)
    
    # Set up environment
    os.environ['GH_ACCESS_TOKEN'] = 'test_token_for_validation'
    
    steps = [
        ("python --version", "Check Python version"),
        ("python -m pip install --upgrade pip", "Upgrade pip"),
        ("python -m pip install uv", "Install uv"),
        ("uv pip install --dev -e .", "Install dependencies"),
        ("uv pip install pytest pytest-cov", "Install test dependencies"),
        ("uv run ruff check gfi/", "Run linting"),
        ("uv run ruff format --check gfi/", "Check formatting"),
        ("uv run pytest gfi/ --cov=gfi --cov-report=html -v", "Run tests with coverage"),
        ("python -m gfi.test_data", "Run data validation tests"),
    ]
    
    passed = 0
    total = len(steps)
    
    for cmd, description in steps:
        if run_command(cmd, description):
            passed += 1
        else:
            print(f"⚠️  Step failed: {description}")
    
    print("\n" + "=" * 60)
    print(f"📊 Results: {passed}/{total} steps passed")
    
    if passed == total:
        print("🎉 All workflow steps passed locally!")
        return 0
    else:
        print("⚠️  Some steps failed - check output above")
        return 1

def test_specific_python_versions():
    """Test with different Python versions if available."""
    print("\n🐍 Testing Multiple Python Versions")
    print("=" * 40)
    
    versions = ['3.9', '3.10', '3.11', '3.12']
    available_versions = []
    
    for version in versions:
        try:
            result = subprocess.run(f"python{version} --version", 
                                  shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                available_versions.append(version)
                print(f"✅ Python {version}: {result.stdout.strip()}")
            else:
                print(f"❌ Python {version}: Not available")
        except:
            print(f"❌ Python {version}: Not available")
    
    if available_versions:
        print(f"\n🎯 Available versions: {', '.join(available_versions)}")
        print("💡 To test matrix strategy, run workflow on each available version")
    else:
        print("⚠️  No alternative Python versions found")

def main():
    """Main test function."""
    # Test current workflow
    result = test_workflow_steps()
    
    # Test Python versions
    test_specific_python_versions()
    
    # Provide recommendations
    print("\n" + "=" * 60)
    print("📋 GitHub Actions Testing Recommendations")
    print("=" * 60)
    print("1. ✅ Local Testing: Completed above")
    print("2. 🌐 GitHub Testing: Push to feature branch")
    print("3. 📊 Coverage: Check htmlcov/index.html after tests")
    print("4. 🔄 CI Monitoring: Watch GitHub Actions tab")
    print("5. 🐛 Debug: Use 'act' tool if available")
    
    return result

if __name__ == '__main__':
    sys.exit(main())
