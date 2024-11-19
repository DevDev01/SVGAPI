from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from svg import SVG, Color, Text, Vector2
import cairosvg
import io

app = FastAPI()

@app.get('/gray/{grayscale}')
def generate_gray(grayscale: int):
    svg = SVG(128, 128)
    svg.background(color=Color(grayscale=grayscale))
    png_data = cairosvg.svg2png(svg.as_string(), output_width=svg.width, output_height=svg.height)
    return StreamingResponse(io.BytesIO(png_data), media_type='image/png')

@app.get('/text/{grayscale}/{text}')
def generate_text(grayscale: int, text: str):
    svg = SVG(64, 128)
    svg.background(color=Color(grayscale=grayscale))
    text = Text(text, Vector2(0, 0))
    text.set_attribute('x', '50%')
    text.set_attribute('y', '50%')
    text.set_attribute('style', 'font-size: 32; font-family: Comic Sans MS;')
    text.set_attribute('text-anchor', 'middle')
    text.set_attribute('dominant-baseline', 'middle')
    svg.add_node(text)
    png_data = cairosvg.svg2png(svg.as_string(), output_width=svg.width, output_height=svg.height)
    return StreamingResponse(io.BytesIO(png_data), media_type='image/png')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='192.168.1.174', port=3000)