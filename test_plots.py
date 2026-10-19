import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def generate_temperature_plot():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    time_pts = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    temp_pts = [42.5, 39.8, 37.2, 35.0, 33.1, 31.6, 30.4, 29.6, 29.0, 28.7]
    ax.plot(time_pts, temp_pts, color='#1A365D', marker='s', markersize=6, linewidth=1.8, label='Effluent Temp')
    ax.set_xlabel('Sampling Time (min)', fontsize=10, fontname='Times New Roman')
    ax.set_ylabel('Effluent Temperature (°C)', fontsize=10, fontname='Times New Roman')
    ax.set_ylim(25, 45)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    plt.close(fig)
    buf.seek(0)
    return buf

def generate_organogram_chart(org_name="HOST ORGANIZATION"):
    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=300)
    ax.axis('off')
    
    # Draw boxes
    boxes = [
        (0.5, 0.88, f"Board of Directors / Managing Director\n{org_name}", '#1A365D', 'white'),
        (0.5, 0.65, "General Manager / Plant Operations Director", '#2B6CB0', 'white'),
        (0.18, 0.38, "Engineering &\nMaintenance Dept.", '#EDF2F7', '#2D3748'),
        (0.50, 0.38, "Operations &\nProduction Dept.", '#EDF2F7', '#2D3748'),
        (0.82, 0.38, "Quality Control &\nHSE Directorate", '#EDF2F7', '#2D3748'),
        (0.18, 0.12, "SIWES Interns &\nTechnical Trainees", '#FEFCBF', '#744210'),
        (0.50, 0.12, "Process Shift\nOperators", '#EDF2F7', '#2D3748'),
        (0.82, 0.12, "Safety &\nInspection Officers", '#EDF2F7', '#2D3748')
    ]
    
    for x, y, text, bg, fg in boxes:
        ax.text(x, y, text, ha='center', va='center', fontsize=7.5, fontname='Times New Roman',
                color=fg, weight='bold',
                bbox=dict(boxstyle='square,pad=0.5', facecolor=bg, edgecolor='#4A5568', linewidth=1))
                
    # Draw connecting lines
    ax.plot([0.5, 0.5], [0.80, 0.73], color='#4A5568', lw=1.5)
    ax.plot([0.5, 0.5], [0.57, 0.48], color='#4A5568', lw=1.5)
    ax.plot([0.18, 0.82], [0.48, 0.48], color='#4A5568', lw=1.5)
    ax.plot([0.18, 0.18], [0.48, 0.45], color='#4A5568', lw=1.5)
    ax.plot([0.50, 0.50], [0.48, 0.45], color='#4A5568', lw=1.5)
    ax.plot([0.82, 0.82], [0.48, 0.45], color='#4A5568', lw=1.5)
    
    ax.plot([0.18, 0.18], [0.31, 0.19], color='#4A5568', lw=1.2, linestyle=':')
    ax.plot([0.50, 0.50], [0.31, 0.19], color='#4A5568', lw=1.2)
    ax.plot([0.82, 0.82], [0.31, 0.19], color='#4A5568', lw=1.2)
    
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    plt.close(fig)
    buf.seek(0)
    return buf

if __name__ == '__main__':
    b1 = generate_temperature_plot()
    b2 = generate_organogram_chart()
    print(f"Plot bytes: {len(b1.getvalue())}, Chart bytes: {len(b2.getvalue())}")
