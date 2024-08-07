#backend/ml/query_processor.py

# import re
# from .code_generation import generate_code
# from .code_fixing import fix_code
# from .code_explanation import explain_code
# from .conversation import generate_response

# def process_query(query):
#     # Check if the query is a code snippet
#     if re.search(r'(def|class|import|from|print|if|for|while)', query):
#         # If it contains common programming keywords, assume it's code
#         if 'error' in query.lower() or 'fix' in query.lower():
#             return fix_code(query)
#         else:
#             return explain_code(query)
#     elif 'generate' in query.lower() and 'code' in query.lower():
#         # If the query asks to generate code
#         return generate_code(query)
#     else:
#         # For all other queries, treat as conversation
#         return generate_response(query)






#backend/ml/conversation.py
