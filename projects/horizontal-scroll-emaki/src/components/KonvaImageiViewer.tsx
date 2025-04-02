"use client";

import { useEffect, useState } from "react";
import { Stage, Layer, Image as KonvaImage } from "react-konva";
import useImage from "use-image";

export default function KonvaImageiViewer() {
  const [isClient, setIsClient] = useState(false);
  const [image] = useImage("/images/hero-image.png", "anonymous");

  useEffect(() => {
    setIsClient(true); // クライアント上でマウントされたら描画
  }, []);

  if (!isClient) return null;

  const width = typeof window !== "undefined" ? window.innerWidth : 800;
  const height = typeof window !== "undefined" ? window.innerHeight : 800;

  return (
    <Stage width={width} height={height} draggable>
      <Layer>{image && <KonvaImage image={image} />}</Layer>
    </Stage>
  );
}
