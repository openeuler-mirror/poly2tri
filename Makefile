CXX = g++
CFLAGS ?= -O2 -g -pipe -Wall
LIBS = -lGL
INCLUDE = -I.
OBJS = common/shapes sweep/advancing_front sweep/cdt sweep/sweep sweep/sweep_context

all: libpoly2tri.so.1.0

libpoly2tri.so.1.0: $(patsubst %,%.o, $(OBJS))
	$(CXX) $(LDFLAGS) -shared -Wl,-soname,libpoly2tri.so.1.0 $^ $(LIBS) -o $@

%.o: %.cc
	$(CXX) $(CFLAGS) $(INCLUDE) -c -fPIC $< -o $@

clean:
	rm -f */*.o libpoly2tri.so*
