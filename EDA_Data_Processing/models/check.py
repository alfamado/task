import joblib
import pprint
import os
# obj = joblib.load(r"C:\Users\NCC200\Desktop\TASK\loan_api\model\preprocessing_artifacts.joblib")
# print(type(obj))
# print(obj.keys())

files = []
for root, _, fnames in os.walk(".", topdown=True):
    for f in fnames:
        if f.endswith(".joblib") or f.endswith(".pkl"):
            files.append(os.path.join(root, f))

print("Found joblib/pkl files:")
pprint.pprint(files)

# Try to load likely candidates and print types/keys (safe try/except)
candidates = files
for f in candidates:
    print("\n---", f)
    try:
        obj = joblib.load(f)
        print("Loaded type:", type(obj))
        # if dict, print keys
        if isinstance(obj, dict):
            print("Keys:", list(obj.keys()))
        # if sklearn pipeline, print steps if possible
        try:
            from sklearn.pipeline import Pipeline
            if isinstance(obj, Pipeline):
                print("Pipeline steps:", obj.named_steps.keys())
        except Exception:
            pass
    except Exception as e:
        print("Could not load (error):", repr(e))
