import os

class VideoConverter:
    def __init__(self, input_path):
        self.input_path = input_path

    def _run_command(self, command):
        os.system(command)

    def resize_video(self):
        resolutions = [(1280, 720, "720p"), (640, 480, "480p"), (360, 240, "360x240"), (160, 120, "160x120")]

        for width, height, name in resolutions:
            output_path = f"{self.input_path}_{name}.mp4"
            command = f'ffmpeg -i "{self.input_path}" -s {width}x{height} -c:a copy "{output_path}"'
            self._run_command(command)

    def convert_to_vp8(self):
        command = f'ffmpeg -i "{self.input_path}" -c:v libvpx -c:a libvorbis "{self.input_path}-VP8.webm"'
        self._run_command(command)

    def convert_to_vp9(self):
        command = f'ffmpeg -i "{self.input_path}" -c:v libvpx-vp9 -c:a libvorbis "{self.input_path}-VP9.webm"'
        self._run_command(command)

    def convert_to_h265(self):
        command = f'ffmpeg -i "{self.input_path}" -c:v libx265 -c:a aac "{self.input_path}-h265.mp4"'
        self._run_command(command)

    def convert_to_h264(self):
        command = f'ffmpeg -i "{self.input_path}" -c:v libx264 -c:a aac "{self.input_path}-h264.mp4"'
        self._run_command(command)

if __name__ == "__main__":
    input_video_path = "BigBuckBunny.mp4"

    # Create the VideoConverter instance
    video_converter = VideoConverter(input_video_path)

    # Resize videos
    video_converter.resize_video()

    # Convert to different codecs
    video_converter.convert_to_vp8()
    video_converter.convert_to_vp9()
    video_converter.convert_to_h265()
    video_converter.convert_to_h264()


