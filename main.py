from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from svg import SVG, Color
import cairosvg
import io


app = FastAPI()

@app.get("/svg/{grayscale}")
def generate_svg(grayscale: int):
    svg = SVG(128, 128)
    svg.background(color=Color(grayscale=grayscale))
    png_data = cairosvg.svg2png(svg.as_string(), output_width=svg.width, output_height=svg.height)
    return StreamingResponse(io.BytesIO(png_data), media_type='image/png')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8080)