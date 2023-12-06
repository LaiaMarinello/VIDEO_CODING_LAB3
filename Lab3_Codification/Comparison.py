import cv2
import os

def compare_videos(video1_path, video2_path, output_path, comment=""):

    width = int(cv2.VideoCapture(video1_path).get(3))
    height = int(cv2.VideoCapture(video1_path).get(4))
    fps = int(cv2.VideoCapture(video1_path).get(5))

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width * 2, height))

    while True:
        ret1, frame1 = cv2.VideoCapture(video1_path).read()
        ret2, frame2 = cv2.VideoCapture(video2_path).read()

        # Concatenate frames side by side
        result_frame = cv2.hconcat([frame1, frame2])

        # Write the result frame
        out.write(result_frame)

    cv2.VideoCapture(video1_path).release()
    cv2.VideoCapture(video2_path).release()
    out.release()

if __name__ == "__main__":
    vp8_video_path = 'BigBuckBunny.mp4-VP8.webm'
    vp9_video_path = 'BigBuckBunny.mp4-VP9.webm'
    output_comparison_path = '/home/laiamarinello/Documents/Lab3_Codification/comparison_output.mp4'

    compare_videos(vp8_video_path, vp9_video_path, output_comparison_path)

##COMENTS: As we can see by comparing the two codecs, VP9 is better since it has higher quality. 
# If we focus our attention on the theoretical part, we know that generally VP9 provides better compression efficiency compared to VP8. 
# Also, it achieves similar visual quality at lower bitrates, making it more suitable for higher resolution videos and streaming.