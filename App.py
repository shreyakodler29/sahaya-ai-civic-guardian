import gradio as gr
from tasks.integrity_scoring import compute_integrity

def run(damage, maintenance, feedback):
    score = compute_integrity(damage, maintenance, feedback)
    return score

gr.Interface(
    fn=run,
    inputs=["slider", "slider", "slider"],
    outputs="number",
    title="Sahaya AI Civic Guardian"
).launch()
