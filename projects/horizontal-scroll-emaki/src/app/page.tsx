"use client";

import Image from "next/image";
import { useEffect, useRef } from "react";

const imageList = Array.from(
  { length: 10 },
  (_, i) =>
    `/images/cyoujyuu_yamazaki_kou_${String(i + 1).padStart(2, "0")}.jpg`
);

export default function Home() {
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ left: 0 });
  }, []);

  return (
    <main className="overflow-x-auto whitespace-nowrap w-full h-screen bg-neutral-100">
      <div
        ref={scrollRef}
        className="flex-row-reverse h-full overflow-x-auto scroll-smooth"
      >
        {imageList.map((src, idx) => (
          <div key={idx} className="flex-shrink-0 w-[100vw] h-full relative">
            <Image
              src={src}
              alt={`Emaki ${idx + 1}`}
              fill
              className="object-contain"
              priority={idx === 0}
            />
          </div>
        ))}
      </div>
    </main>
  );
}
