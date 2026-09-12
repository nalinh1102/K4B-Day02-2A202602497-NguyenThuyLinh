import streamlit as st

st.set_page_config(
    page_title="PR Context Copilot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 PR Context Copilot")
st.write("AI hỗ trợ tổng hợp context trước khi review Pull Request")

st.divider()

pr_name = st.text_input(
    "Pull Request",
    "PR #128 - Fix authentication bug"
)

ticket = st.text_input(
    "Related Ticket",
    "AUTH-142"
)

if st.button("ANALYZE PR"):
    st.subheader("AI REVIEW BRIEF")

    st.markdown("""
### Summary
Fix authentication issue related to expired access tokens.

### Related Ticket
AUTH-142

### Changed Files
- auth.py
- login_service.py
- token_validator.py

### Key Changes
- Token validation logic changed
- Login error handling changed
- Token expiration check added

### Areas to Review
- Authentication logic
- Token expiration behavior
- Error handling

### Review Checklist
- [ ] Check authentication validation
- [ ] Check expired-token behavior
- [ ] Check error handling
- [ ] Check related tests

⚠️ **AI-generated suggestion. Reviewer must verify before approval.**
""")