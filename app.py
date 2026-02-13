import streamlit as st
from streamlit_echarts import st_echarts

# 1. Page Configuration
st.set_page_config(page_title="Mind Map Pro", layout="wide")

# 2. Initialize Data Structure
if 'mind_map_data' not in st.session_state:
    st.session_state.mind_map_data = {
        "name": "My Main Goal",
        "children": []
    }

# 3. Sidebar Interface
with st.sidebar:
    st.header("🛠️ Map Controls")
    
    # Edit the Root
    new_root = st.text_input("Rename Central Topic", st.session_state.mind_map_data["name"])
    st.session_state.mind_map_data["name"] = new_root

    st.divider()

    # Add a Node
    st.subheader("Add a Branch")
    node_name = st.text_input("New Node Name", placeholder="e.g., Budget")
    if st.button("➕ Add Node", use_container_width=True):
        if node_name:
            st.session_state.mind_map_data["children"].append({"name": node_name, "children": []})
            st.rerun()

    st.divider()

    # Delete last node
    if st.button("🗑️ Remove Last Node", type="primary", use_container_width=True):
        if st.session_state.mind_map_data["children"]:
            st.session_state.mind_map_data["children"].pop()
            st.rerun()

# 4. Main Canvas
st.title("🧠 Interactive Mind Map")
st.write("Click nodes to expand/collapse. Use the sidebar to edit.")

# 5. ECharts Configuration
chart_options = {
    "series": [{
        "type": "tree",
        "data": [st.session_state.mind_map_data],
        "top": "5%",
        "left": "15%",
        "bottom": "5%",
        "right": "15%",
        "symbolSize": 15,
        "initialTreeDepth": 2,
        "label": {
            "position": "top",
            "rotate": 0,
            "verticalAlign": "middle",
            "align": "center",
            "fontSize": 14,
            "fontWeight": "bold"
        },
        "leaves": {
            "label": {
                "position": "bottom",
                "verticalAlign": "middle",
                "align": "center"
            }
        },
        "emphasis": {"focus": "descendant"},
        "expandAndCollapse": True,
        "animationDuration": 600,
    }]
}

# 6. Render
st_echarts(options=chart_options, height="600px")

# 7. Data Export (Optional)
with st.expander("📂 Export Map Data"):
    st.json(st.session_state.mind_map_data)
  
