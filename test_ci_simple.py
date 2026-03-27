#!/usr/bin/env python
"""Simple CI workflow testing script."""

import subprocess
import sys
import os

def run_step(cmd, description):
    """Run a single CI step."""
    print(f"\n🔄 {description}")
    print(f"Command: {cmd}")
    print("-" * 40)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ PASSED")
            if result.stdout.strip():
                print(f"Output: {result.stdout.strip()}")
        else:
            print("❌ FAILED")
            if result.stderr.strip():
                print(f"Error: {result.stderr.strip()}")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")
        return False

def main():
    """Test CI workflow steps."""
    print("🧪 Testing GitHub Actions Workflow Steps")
    print("=" * 50)
    
    # Set environment
    os.environ['GH_ACCESS_TOKEN'] = 'test_token'
    
    # Test core steps that don't require uv
    steps = [
        ("python --version", "Check Python version"),
        ("python -c \"import gfi.config; print('Config module OK')\"", "Test config module"),
        ("python -c \"import gfi.utils; print('Utils module OK')\"", "Test utils module"),
        ("python -c \"import gfi.github_api; print('GitHub API module OK')\"", "Test GitHub API module"),
        ("python -c \"import gfi.populate; print('Populate module OK')\"", "Test populate module"),
        ("python -m gfi.test_data", "Run data validation tests"),
    ]
    
    passed = 0
    total = len(steps)
    
    for cmd, desc in steps:
        if run_step(cmd, desc):
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} steps passed")
    
    if passed == total:
        print("🎉 All core CI steps work locally!")
        print("💡 Next: Push to GitHub to test full workflow")
        return 0
    else:
        print("⚠️  Some steps failed - check above")
        return 1

if __name__ == '__main__':
    sys.exit(main())
