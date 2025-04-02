"use client";

import { useEffect, useState } from "react";
import { Stage, Layer, Image as KonvaImage } from "react-konva";
import useImage from "use-image";

export default function EmakiViewer() {
  const [isMounted, setIsMounted] = useState(false);

  const [image1] = useImage("/images/cyoujyuu_yamazaki_kou_01.jpg");
  const [image2] = useImage("/images/cyoujyuu_yamazaki_kou_02.jpg");

  useEffect(() => {
    setIsMounted(true);
  }, []);

  // 画像ロード後にサイズ取得してキャンバス幅を調整する
  const stageWidth = (image1?.width || 0) + (image2?.width || 0);
  const stageHeight = Math.max(image1?.height || 0, image2?.height || 0);

  if (!isMounted) return null;

  return (
    <div
      style={{
        width: `${stageWidth}px`,
        height: stageHeight,
        overflowX: "scroll",
        background: "#fefefe",
      }}
    >
      <Stage width={stageWidth} height={stageHeight}>
        <Layer>
          {image2 && <KonvaImage image={image2} x={0} y={0} />}
          {image1 && (
            <KonvaImage
              image={image1}
              x={image1?.width || 0} // 1枚目の右隣に表示
              y={0}
            />
          )}
        </Layer>
      </Stage>
    </div>
  );
}
