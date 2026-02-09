
import os
from dotenv import load_dotenv

# Force reload dotenv
load_dotenv(override=True)

try:
    print(f"sir_token in env: {'sir_token' in os.environ}")
    if 'sir_token' in os.environ:
        print(f"sir_token length: {len(os.environ['sir_token'])}")
        # print(f"sir_token value: {os.environ['sir_token']}") # Be careful not to print secrets if possible, or print partial

    # Import the function - this might fail if client init fails
    from utils.ai_response import get_completion
    
    print("Calling get_completion...")
    response = get_completion("Hello", "You are a helpful assistant.")
    print("Response:", response)

except Exception as e:
    print("Caught exception:")
    print(e)
    import traceback
    traceback.print_exc()
